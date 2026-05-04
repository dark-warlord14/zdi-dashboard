# ZDI-10-069: Microsoft Office Publisher File Conversion TextBox Processing Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-069
- **ZDI-CAN:** ZDI-CAN-612
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0479
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Publisher
- **Credit:** Lionel d'Hauenens (www.laboskopia.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires user interaction in that a victim must open a malicious PUB file. The specific flaw exists within the code responsible for converting files from the Publisher 97 format. While processing a TextBox item, several programming errors can be triggered allowing a maliciously created publisher file to execute arbitrary code under the context of the user opening the file.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-023.mspx

## Disclosure Timeline

- 2009-11-06 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
