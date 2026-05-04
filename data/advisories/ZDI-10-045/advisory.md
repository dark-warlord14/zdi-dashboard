# ZDI-10-045: Apple QuickTime MPEG-1 genl Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-045
- **ZDI-CAN:** ZDI-CAN-608
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0526
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of MPEG content. Upon reading a field used for compression within a 'genl' atom in the movie container, the application will decompress outside the boundary of an allocated buffer. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

http://support.apple.com/kb/HT4104 http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-11-06 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
