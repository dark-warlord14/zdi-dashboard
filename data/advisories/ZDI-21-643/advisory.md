# ZDI-21-643: Bosch B426 Web Configuration Credential Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-643
- **ZDI-CAN:** ZDI-CAN-13075
- **Date:** 2021-06-02
- **CVE:** CVE-2021-23846
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bosch
- **Affected Products:** B426
- **Credit:** Chizuru Toyama of TXOne IoT/ICS Security Research Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-643/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Bosch B426. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of login credentials provided to the login.cgi endpoint. The issue results from displaying sensitive information in plaintext. An attacker can leverage this vulnerability to disclose sensitive information in the context of the user.

## Additional Details

Bosch has issued an update to correct this vulnerability. More details can be found at: https://psirt.bosch.com/security-advisories/bosch-sa-196933-bt.html

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-06-02 - Coordinated public release of advisory
- 2021-06-03 - Advisory Updated
