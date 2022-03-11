/**
 * FormValidation (https://formvalidation.io)
 * The best validation library for JavaScript
 * (c) 2013 - 2019 Nguyen Huu Phuoc <me@phuoc.ng>
 */

import jmbg from './jmbg';

/**
 * @returns {ValidateResult}
 */
export default function rsId(value: string) {
    return {
        meta: {},
        valid: jmbg(value, 'RS'),
    };
}
