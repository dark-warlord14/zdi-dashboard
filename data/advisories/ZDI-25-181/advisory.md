# ZDI-25-181: (0Day) Arista NG Firewall User-Agent Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-181
- **ZDI-CAN:** ZDI-CAN-24407
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2767
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Gereon Huppertz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Arista NG Firewall. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the processing of the User-Agent HTTP header. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

09/13/24 – ZDI reported the vulnerability to the vendor 01/08/25 - ZDI asked for updates 03/12/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-09-13 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
