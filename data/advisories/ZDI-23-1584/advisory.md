# ZDI-23-1584: SolarWinds Orion Platform BlacklistedFilesChecker Incomplete List of Disallowed Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1584
- **ZDI-CAN:** ZDI-CAN-21839
- **Date:** 2023-11-06
- **CVE:** CVE-2023-40062
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1584/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the BlacklistedFilesChecker class. The issue results from an incomplete list of disallowed inputs. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2023-40062

## Disclosure Timeline

- 2023-08-03 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory
