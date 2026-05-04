# ZDI-20-1009: Parallels Desktop prl_hypervisor Exposed Dangerous Method Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1009
- **ZDI-CAN:** ZDI-CAN-10518
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17391
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1009/
## Vulnerability Details

This vulnerability allows local attackers to disclose information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handler for HOST_IOCTL_INIT_HYPERVISOR in the prl_hypervisor kext. The issue results from the exposure of dangerous method or function to the unprivileged user. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-04-01 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
