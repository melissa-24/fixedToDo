class Footer extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <footer>
                <h3>Created by Melissa Longenberger</h3>
            </footer>
        `;
    }
}

customElements.define('footer-component', Footer);