# ZDI-10-104: Microsoft Office Excel SxView Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-104
- **ZDI-CAN:** ZDI-CAN-498
- **Date:** 2010-06-08
- **CVE:** CVE-2010-0821
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must open a malicious document. The specific flaw exists in the parsing of SXVIEW records in an Excel spreadsheet. Due to the lack of checking when parsing structure items for the record it is possible to write arbitrary data to a user controlled address. Successful exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
- 2021-07-15 - Advisory Updated
