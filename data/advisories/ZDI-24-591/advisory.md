# ZDI-24-591: Linux Kernel RSVP Filter Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-591
- **ZDI-CAN:** ZDI-CAN-18387
- **Date:** 2024-06-10
- **CVE:** CVE-2023-42755
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:L/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-591/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of RSVP filters. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2239847

## Disclosure Timeline

- 2022-08-19 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
