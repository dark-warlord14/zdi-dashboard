# ZDI-23-1032: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway GTWWebMonitorService Unquoted Search Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1032
- **ZDI-CAN:** ZDI-CAN-20538
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39464
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1032/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the GTWWebMonitorService service. The path to the service executable contains spaces not surrounded by quotations. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
