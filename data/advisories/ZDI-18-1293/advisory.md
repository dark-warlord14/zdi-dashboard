# ZDI-18-1293: Trend Micro Anti-Virus UrlfWTPPagePtr KERedirect Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1293
- **ZDI-CAN:** ZDI-CAN-6368
- **Date:** 2018-10-19
- **CVE:** CVE-2018-15366
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Anti-Virus
- **Credit:** vms
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1293/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Anti-Virus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the UrlfWTPPagePtr variable in the KERedirect kext. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-US/home/pages/technical-support/1121296.aspx

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-10-19 - Coordinated public release of advisory
- 2018-10-19 - Advisory Updated
