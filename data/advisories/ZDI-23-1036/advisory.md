# ZDI-23-1036: Triangle MicroWorks SCADA Data Gateway DbasSectorFileToExecuteOnReset Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1036
- **ZDI-CAN:** ZDI-CAN-20799
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39468
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Uri Katz of Claroty Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of DbasSectorFileToExecuteOnReset parameter. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
