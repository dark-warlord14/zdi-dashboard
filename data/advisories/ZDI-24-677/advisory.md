# ZDI-24-677: (0Day) Dropbox Desktop Folder Sharing Mark-of-the-Web Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-677
- **ZDI-CAN:** ZDI-CAN-23991
- **Date:** 2024-06-13
- **CVE:** CVE-2024-5924
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dropbox
- **Affected Products:** Dropbox Desktop
- **Credit:** Peter Girnus (@gothburz)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-677/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-of-the-Web protection mechanism on affected installations of Dropbox Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of shared folders. When syncing files from a shared folder belonging to an untrusted account, the Dropbox desktop application does not apply the Mark-of-the-Web to the local files. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

06/05/24 – ZDI reported the vulnerability to the vendor. 06/06/24 – The vendor acknowledged the report. 06/10/24 – The vendor states the vulnerability about Mark-of-the-Web is out of scope for their bug bounty program. 06/11/24 – ZDI acknowledged their rejection and informed the vendor that we’re publishing this case as a zero-day advisory on 6/13/24 in accordance with our disclosure policy. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-06-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
