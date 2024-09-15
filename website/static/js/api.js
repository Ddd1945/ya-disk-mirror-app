function getDiskData(dirPath = null, goBack = false) {
  $(".loader_container").css("visibility", "visible");

  if (goBack) {
    let currentDirPath = localStorage.getItem("currentDirPath");

    if (currentDirPath) {
      let newDirPath = currentDirPath.substring(
        0,
        currentDirPath.lastIndexOf("/")
      );

      dirPath = newDirPath;

      localStorage.setItem("currentDirPath", newDirPath);
    }
  }

  let diskLink = $("#directory_link").val();

  $.ajax({
    url: "/get-disk-data",
    method: "GET",
    data: { dir_path: dirPath, disk_link: diskLink },
    success: function (response) {
      localStorage.setItem("currentDirPath", dirPath);

      disk_files_container = $("#disk_files");

      items = response.data;

      disk_files_container.empty();

      for (let i = 0; i < items.length; i++) {
        $("#disk_files").append(
          `
            <span class="disk_item">
                <img src="${items[i].image_link}" width="21 " height="21" />
                <div class="clickable_text">${items[i].name}</div>
            </span>
          `
        );

        $(".clickable_text")[i].addEventListener("click", function () {
          if (items[i]?.type === "dir") getDiskData(items[i]?.path);
          else handleYaDownload(items[i].file, items[i].name);
        });
      }
    },
    error: function (xhr, status, error) {
      console.log("Error at getDiskData: " + error);
    },
    complete: function () {
      $(".loader_container").css("visibility", "hidden");
    },
  });
}

function handleYaDownload(link, name) {
  $(".loader_container").css("visibility", "visible");

  $.ajax({
    url: "/handle-ya-download",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({ link: link, name: name }),
    xhrFields: {
      responseType: "blob",
    },
    success: function (data, status, xhr) {
      const blob = new Blob([data], {
        type: xhr.getResponseHeader("Content-Type"),
      });

      const url = window.URL.createObjectURL(blob);

      const $a = $("<a></a>");

      $a.attr("href", url);

      const contentDisposition = xhr.getResponseHeader("Content-Disposition");

      if (contentDisposition) {
        const matches = /filename="([^"]+)"/.exec(contentDisposition);

        if (matches != null && matches[1]) name = matches[1];
      }

      $a.attr("download", name);

      $("body").append($a);

      $a[0].click();

      $a.remove();

      window.URL.revokeObjectURL(url);
    },
    error: function (xhr, status, error) {
      console.log("Error at `handleYaDownload`: " + error);
    },
    complete: function () {
      $(".loader_container").css("visibility", "hidden");
    },
  });
}
