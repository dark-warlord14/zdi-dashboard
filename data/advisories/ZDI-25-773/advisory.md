# ZDI-25-773: (0Day) Google Drive File Sharing Mark-of-the-Web Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-773
- **ZDI-CAN:** ZDI-CAN-24742
- **Date:** 2025-08-05
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Drive
- **Credit:** Peter Girnus (@gothburz)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-773/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-of-the-Web protection mechanism on affected installations of Google Drive. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Google Drive desktop application for Windows. When syncing files shared from a untrusted account, the Google Drive desktop application does not apply the Mark-of-the-Web to the local copies of the files. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

07/12/24 – ZDI reported the vulnerability to the vendor. 07/12/24 – The vendor acknowledged the report. 07/26/24 – The vendor states the issue might not be severe enough to track as an abuse risk and the case does not meet the threshold for a fix. 07/30/24 – ZDI provided details as to why we disagree with their assessment. 08/19/24 – The vendor states that they reviewed the case again, and that their assessment remains unchanged. 07/31/25 – After careful review the ZDI decided that this case should be disclosed publicly on 08/05/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-07-05 - Vulnerability reported to vendor
- 2025-08-05 - Coordinated public release of advisory
- 2025-08-05 - Advisory Updated
