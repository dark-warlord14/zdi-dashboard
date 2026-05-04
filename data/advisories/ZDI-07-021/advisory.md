# ZDI-07-021: GraceNote CDDBControl ActiveX Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-021
- **ZDI-CAN:** ZDI-CAN-087
- **Date:** 2007-04-19
- **CVE:** CVE-2007-0443
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** GraceNote
- **Affected Products:** ActiveX CDDB Control
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-021/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of GraceNote's CDDBControl ActiveX Control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists due to a buffer overflow in an ActiveX control registered by several products that use Gracenote CDDB for CD information lookup. The ActiveX control is commonly registered as safe and can be accessed from a malicious web site. The buffer overflow is triggered when long values are specified for various Proxy configuration parameters.

## Additional Details

GraceNote has issued an update to correct this vulnerability. More details can be found at: http://www.gracenote.com/corporate/FAQs.html/faqset=update/page=0

## Disclosure Timeline

- 2006-09-01 - Vulnerability reported to vendor
- 2007-04-19 - Coordinated public release of advisory
