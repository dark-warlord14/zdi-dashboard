# ZDI-19-470: Microsoft Edge CDXImageRenderTarget Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-470
- **ZDI-CAN:** ZDI-CAN-8376
- **Date:** 2019-05-15
- **CVE:** CVE-2019-0940
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Arthur Gerkis of Exodus Intelligence (@ax330d)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-470/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the rendering of pattern images within HTML canvas elements. By manipulating a document's elements, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0940

## Disclosure Timeline

- 2019-05-15 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
