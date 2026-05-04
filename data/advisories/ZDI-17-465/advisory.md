# ZDI-17-465: Fatek Automation PLC Ethernet Module Configuration Tool Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-465
- **ZDI-CAN:** ZDI-CAN-3706
- **Date:** 2017-07-11
- **CVE:** CVE-2017-6023
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fatek Automation
- **Affected Products:** PLC Ethernet Module Configuration Tool
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-465/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fatek Automation PLC Ethernet Module Configuration Tool. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ether_cfg.exe. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-073-01

## Disclosure Timeline

- 2016-07-19 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
