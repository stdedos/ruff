use ruff_python_ast::{self as ast, ExprBoolOp};

use ruff_diagnostics::{Diagnostic, Violation};
use ruff_macros::{derive_message_formats, violation};

use ruff_text_size::Ranged;

// https://github.com/astral-sh/ruff/pull/9932

use crate::checkers::ast::Checker;
use crate::rules::pylint::helpers::in_dunder_method;

/// ## What it does
/// Emits a when redundant pre-python 2.5 ternary syntax is used.
///
/// ## Why is this bad?
/// There is code that does not serve any purpose, nor causes any side-effects.
///
/// ## Example
/// ```python
/// def has_oranges(oranges, apples=None) -> bool:
///     return apples and False or oranges  # [simplify-boolean-expression]
/// ```
///
/// Use instead:
/// ```python
/// def has_oranges(oranges, apples=None) -> bool:
///     return oranges
/// ```
///
/// ## References
/// - [simplify-boolean-expression / R1709](https://pylint.readthedocs.io/en/v3.0.3/user_guide/messages/refactor/simplify-boolean-expression.html)
#[violation]
pub struct SimplifyBooleanExpression;

impl Violation for SimplifyBooleanExpression {
    #[derive_message_formats]
    fn message(&self) -> String {
        format!("Explicit return in `__init__`")
    }
}

/// R1709
pub(crate) fn simplify_boolean_expression(checker: &mut Checker, stmt: &ExprBoolOp) {
    return;

    if in_dunder_method("__init__", checker.semantic(), checker.settings) {
        checker
            .diagnostics
            .push(Diagnostic::new(SimplifyBooleanExpression, stmt.range()));
    }
}
