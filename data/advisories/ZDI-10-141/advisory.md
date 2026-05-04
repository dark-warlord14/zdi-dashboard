# ZDI-10-141: Apple Webkit SVG ForeignObject Rendering Layout Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-141
- **ZDI-CAN:** ZDI-CAN-766
- **Date:** 2010-08-05
- **CVE:** CVE-2010-1786
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-141/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Webkit's layout implementation of an particular tag used for embedding a foreign document into the SVG namespace. Later when the application attempts to calculate layout information for rendering the contents of the tag, the application will attempt to access a linebox that was previously destroyed. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4276

## Disclosure Timeline

- 2010-05-03 - Vulnerability reported to vendor
- 2010-08-05 - Coordinated public release of advisory
