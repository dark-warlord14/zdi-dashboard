# ZDI-24-1184: Progress Software WS_FTP Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1184
- **ZDI-CAN:** ZDI-CAN-22322
- **Date:** 2024-08-29
- **CVE:** CVE-2024-7744
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** WS_FTP
- **Credit:** Le Ngoc Anh (@L3ng0c4nh) of Sun* CSR and @dieulink of NCSC VietNam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1184/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software WS_FTP. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileHandler module. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of NETWORK SERVICE.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WS-FTP-Server-Service-Pack-August-2024

## Disclosure Timeline

- 2024-05-15 - Vulnerability reported to vendor
- 2024-08-29 - Coordinated public release of advisory
- 2024-08-29 - Advisory Updated
