# ZDI-25-980: Heimdall Data Database Proxy Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-980
- **ZDI-CAN:** ZDI-CAN-24755
- **Date:** 2025-10-30
- **CVE:** CVE-2025-12486
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Heimdall Data
- **Affected Products:** Database Proxy
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-980/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Heimdall Data Database Proxy. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the handling of the database event logs. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to interact with the application in the context of the target user.

## Additional Details

Fixed in release build 25.03.01.10 https://www.heimdalldata.com/release-notes/

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-10-30 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated
