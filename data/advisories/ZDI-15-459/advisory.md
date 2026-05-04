# ZDI-15-459: Microsoft Internet Explorer CIERegistryHelper::SetSingleValue Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-459
- **ZDI-CAN:** ZDI-CAN-2941
- **Date:** 2015-10-07
- **CVE:** CVE-2015-2429
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-459/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CIERegistryHelper::SetSingleValue API. When this API is used with a whitelisted registry entry, an attacker can modify privileged registry values via a registry link. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-090.aspx

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-10-07 - Coordinated public release of advisory
