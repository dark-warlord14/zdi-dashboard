# ZDI-23-1029: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Event Log Improper Output Neutralization For Logs Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1029
- **ZDI-CAN:** ZDI-CAN-20535
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39461
- **CVSS:** 4.4
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1029/
## Vulnerability Details

This vulnerability allows remote attackers to write arbitrary files on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of event logs. The issue results from improper sanitization of log output. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
