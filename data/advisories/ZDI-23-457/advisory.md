# ZDI-23-457: SolarWinds Network Performance Monitor ExecuteExternalProgram Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-457
- **ZDI-CAN:** ZDI-CAN-17702
- **Date:** 2023-04-24
- **CVE:** CVE-2022-36963
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-457/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the ExecuteExternalProgram method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/CVE-2022-36963

## Disclosure Timeline

- 2022-06-24 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
