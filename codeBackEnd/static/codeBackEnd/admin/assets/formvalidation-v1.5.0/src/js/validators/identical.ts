/**
 * FormValidation (https://formvalidation.io)
 * The best validation library for JavaScript
 * (c) 2013 - 2019 Nguyen Huu Phuoc <me@phuoc.ng>
 */

import { Localization, ValidateInput, ValidateOptions, ValidateResult } from '../core/Core';

type CompareWithCallback = () => string;

export interface IdenticalOptions extends ValidateOptions {
    compare: string | CompareWithCallback;
}

export default function identical() {
    return {
        validate(input: ValidateInput<IdenticalOptions, Localization>): ValidateResult {
            const compareWith = ('function' === typeof input.options.compare)
                ? (input.options.compare as CompareWithCallback).call(this)
                : (input.options.compare as string);

            return {
                valid: (compareWith === '' || input.value === compareWith),
            };
        },
    };
}
