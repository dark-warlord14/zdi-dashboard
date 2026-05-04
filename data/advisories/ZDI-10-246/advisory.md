# ZDI-10-246: Microsoft Excel MSODrawing Improper Exception Handling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-246
- **ZDI-CAN:** ZDI-CAN-855
- **Date:** 2010-11-09
- **CVE:** CVE-2010-3335
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-246/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application frees resources when parsing a malformed Office Art record. Due to the application not properly freeing up resources during handling a parsing error, the application will later access the freed reference which can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-087.mspx

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-11-09 - Coordinated public release of advisory
