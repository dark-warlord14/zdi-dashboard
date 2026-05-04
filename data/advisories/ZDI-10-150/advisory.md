# ZDI-10-150: Microsoft Office Word sprmCMajority Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-150
- **ZDI-CAN:** ZDI-CAN-527
- **Date:** 2010-08-11
- **CVE:** CVE-2010-1900
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** L.W.Z of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must open a malicious document. The specific flaw exists in the parsing of sprmCMajority records in a Word document. Due to the lack of parameter checking when processing sprmCMajority sprm groups it is possible to arbitrarily control the amount of data being written to a stack based buffer resulting in a stack overflow vulnerability which can overwrite critical exception structures. Successful exploitation can lead to remote code execution under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-056.mspx

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-08-11 - Coordinated public release of advisory
