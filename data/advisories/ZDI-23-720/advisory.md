# ZDI-23-720: Moxa MXsecurity Series Hardcoded JWT Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-720
- **ZDI-CAN:** ZDI-CAN-19896
- **Date:** 2023-05-24
- **CVE:** CVE-2023-33236
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Moxa
- **Affected Products:** MXsecurity Series
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-720/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Moxa MXsecurity Series appliances. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the web-based interface. The issue results from a hardcoded JWT secret within the application configuration. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://www.moxa.com/en/support/product-support/security-advisory/mxsecurity-command-injection-and-hardcoded-credential-vulnerabilities

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
