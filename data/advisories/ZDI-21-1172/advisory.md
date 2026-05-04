# ZDI-21-1172: Fatek Automation WinProladder PLC Configuration Data Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1172
- **ZDI-CAN:** ZDI-CAN-13790
- **Date:** 2021-10-14
- **CVE:** CVE-2021-38442
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** WinProladder
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation WinProladder. User interaction is required to exploit this vulnerability in that the target must access a compromised device or a device on a compromised network. The specific flaw exists within the parsing of PLC configuration data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-280-06

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
