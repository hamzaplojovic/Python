const generateLink = () => {
    const linkElement = document.getElementById("mailLink");
    const subject = document.getElementById("subject").value;
    const body = document.getElementById("body").value;

    linkElement.href = `mailto:hamzaplojovic9@gmail.com?subject=${subject}&body=${body}`;
};
