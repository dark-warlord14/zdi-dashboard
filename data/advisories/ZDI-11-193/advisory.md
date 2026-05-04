# ZDI-11-193: Microsoft Internet Explorer DOM Modification Race Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-193
- **ZDI-CAN:** ZDI-CAN-1020
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1256
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application handles multiple javascript modifications to the document. In certain instances the application will free an object due to a modification and then later access it again when attempting to destroy it. This re-use can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-050.mspx

## Disclosure Timeline

- 2011-02-28 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
