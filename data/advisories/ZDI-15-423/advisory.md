# ZDI-15-423: Microsoft Internet Explorer ISettingsBroker Sandbox Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-423
- **ZDI-CAN:** ZDI-CAN-2939
- **Date:** 2015-09-08
- **CVE:** CVE-2015-2489
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 5AECDBC12A3C178E19CF1E3CB5EDAA89
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-423/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of ISettingsBroker. By using a specified CLSID to the setValue method, an attacker can modify privileged registry values. An attacker can leverage this vulnerability to execute code under the context of the user at Medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-094

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
