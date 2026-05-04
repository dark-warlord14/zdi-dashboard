# ZDI-22-1460: SolarWinds Network Performance Monitor PropertyBagJsonConverter Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1460
- **ZDI-CAN:** ZDI-CAN-17530
- **Date:** 2022-10-21
- **CVE:** CVE-2022-36957
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1460/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the PropertyBagJsonConverter. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2022-36957

## Disclosure Timeline

- 2022-05-27 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
