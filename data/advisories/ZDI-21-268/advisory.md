# ZDI-21-268: (0Day) Lepide Active Directory Self Service Unsafe Interaction Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-268
- **ZDI-CAN:** ZDI-CAN-11708
- **Date:** 2021-03-11
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lepide
- **Affected Products:** Active Directory Self Service
- **Credit:** Antoine Cervoise & Quentin Rouves both from NTT.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-268/
## Vulnerability Details

This vulnerability allows physical or remote attackers to bypass the Windows login screen on affected installations of Lepide Active Directory Self Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the "Reset Password / Unlock Account" feature. By interacting with this feature, an attacker can launch a highly-privileged web browser. An attacker can leverage this vulnerability to bypass the Windows login screen and execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/16/20 – ZDI reported the vulnerability to the vendor 01/20/21 – ZDI requested an update 02/03/21 – ZDI requested an update and notified the vendor of the intention to publish the case as a 0-day advisory on 02/11/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-09-16 - Vulnerability reported to vendor
- 2021-03-11 - Coordinated public release of advisory
