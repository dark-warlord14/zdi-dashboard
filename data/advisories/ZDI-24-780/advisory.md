# ZDI-24-780: PaperCut NG upload Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-780
- **ZDI-CAN:** ZDI-CAN-23074
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1221
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-780/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of PaperCut NG. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the upload endpoint. By uploading a symbolic link, an attacker can abuse the service to read arbitrary files. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
