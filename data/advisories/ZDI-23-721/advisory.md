# ZDI-23-721: Moxa MXsecurity Series Restricted Shell Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-721
- **ZDI-CAN:** ZDI-CAN-19895
- **Date:** 2023-05-24
- **CVE:** CVE-2023-33235
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Moxa
- **Affected Products:** MXsecurity Series
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-721/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Moxa MXsecurity Series appliances. Authentication is required to exploit this vulnerability. The specific flaw exists within the SSH CLI program. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the administrative user.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://www.moxa.com/en/support/product-support/security-advisory/mxsecurity-command-injection-and-hardcoded-credential-vulnerabilities

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
