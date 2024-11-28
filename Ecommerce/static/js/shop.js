const categories = document.querySelectorAll('.categories a');
const contents = document.querySelectorAll('.main-content > div');

categories.forEach((category, index) => {
  category.addEventListener('click', () => {
    contents.forEach((content) => {
      content.hidden = true;
    });
    contents[index].hidden = false;
  });
});