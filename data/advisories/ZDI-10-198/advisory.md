# ZDI-10-198: Microsoft Internet Explorer EOT File hdmx Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-198
- **ZDI-CAN:** ZDI-CAN-833
- **Date:** 2010-10-12
- **CVE:** CVE-2010-1883
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of an Embedded OpenType file to TrueType format within t2embed.dll. The most likely vector for this to be exploited is via Internet Explorer as an embedded font in an HTML/CSS document. The flaw itself is due to an integer overflow when parsing hdmx records. A record size and record count variable are trusted and operated upon. The resulting value is used in a copy loop that can be manipulated to corrupt memory. This can be abused by an attacker to execute remote code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-076.mspx

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
