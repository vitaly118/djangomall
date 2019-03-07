import React, { useState } from 'react';
import ReactDOM from 'react-dom';

import { Example } from './components/Example';

document.addEventListener('DOMContentLoaded', (event) => {
      ReactDOM.render(<Example />, document.getElementById('app'));
});
