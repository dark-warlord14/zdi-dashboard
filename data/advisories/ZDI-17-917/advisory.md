# ZDI-17-917: Microsoft Windows EngLockSurface Time-Of-Check Time-Of-Use Race Condition Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-917
- **ZDI-CAN:** ZDI-CAN-5131
- **Date:** 2017-11-20
- **CVE:** CVE-2017-11851
- **CVSS:** 5.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-917/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the EngLockSurface API. Performing a memory write at an unexpected time during the execution of EngLockSurface can cause the kernel to read from an improper address. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11851

## Disclosure Timeline

- 2017-09-01 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
