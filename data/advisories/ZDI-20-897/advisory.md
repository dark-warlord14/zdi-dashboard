# ZDI-20-897: Oracle Java Runtime Environment HTML Rendering Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-897
- **ZDI-CAN:** ZDI-CAN-10965
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14664
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime Environment
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-897/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Java Runtime Environment. Interaction with the JavaFX library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the rendering of HTML in JavaFX. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-05-06 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
