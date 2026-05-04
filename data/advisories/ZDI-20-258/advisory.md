# ZDI-20-258: Microsoft Exchange Server Exchange Control Panel Fixed Cryptographic Key Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-258
- **ZDI-CAN:** ZDI-CAN-9615
- **Date:** 2020-02-20
- **CVE:** CVE-2020-0688
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the Exchange Control Panel web application. The product fails to generate a unique cryptographic key at installation, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0688

## Disclosure Timeline

- 2019-11-26 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
