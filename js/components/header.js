class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <header>
                <h1>Bee Productive</h1>
                <nav>
                    <a href='index.html'>Home</a>
                    <a href='about.html'>About</a>
                    <a href='month.html'>Month</a>
                    <a href='day.html'>Day</a>
                </nav>
            </header>
        `;
    }
}

customElements.define('header-component', Header);