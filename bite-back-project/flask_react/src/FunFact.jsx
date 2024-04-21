
/**
 * Image Credit
 * Image by <a href="https://pixabay.com/users/daria-yakovleva-3938704/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1932466">Дарья Яковлева</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1932466">Pixabay</a>
 */
/**Nutrition Fact Credit
 * Centers for Disease Control and Prevention
 * https://www.cdc.gov/nutrition/about-nutrition/why-it-matters.html
 */

export default function FunFact() {
    return (
      <div className="funFactContainer">
        <div className="funFactImage">
            <img src="https://cdn.pixabay.com/photo/2016/12/26/17/28/spaghetti-1932466_1280.jpg" alt="Fresh Food"></img>
        </div>
        <div className="funFactText">
            <h2>Fewer than 1 in 10 children and adults eat the recommended daily amount of vegetables</h2>
            <p>According to the <a href="https://www.cdc.gov/nutrition/about-nutrition/why-it-matters.html">CDC</a>, "good nutrition is essential in keeping current and future generations of Americans healthy." People who eat healthy have less of a risk for "heart disease, type 2 diabetes, and obesity."</p>
        </div>
      </div>
    );
  }