# ZDI-10-041: Apple QuickTime QDM2/QDCA Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-041
- **ZDI-CAN:** ZDI-CAN-546
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0059
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the rendering of an audio stream utilizing QDesign's audio codec. The application will perform an allocation utilizing a field specified in the sample's description. Later when initializing the buffer, the application will utilize a different length. If the lengths differ, then a buffer overflow will occur. This can lead to code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
