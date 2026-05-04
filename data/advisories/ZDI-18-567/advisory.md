# ZDI-18-567: Qemu Slirp Networking Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-567
- **ZDI-CAN:** ZDI-CAN-5588
- **Date:** 2018-06-07
- **CVE:** CVE-2018-11806
- **CVSS:** 3.7
- **CVSS Vector:** AV:L/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Qemu
- **Affected Products:** Qemu
- **Credit:** jskz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-567/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Qemu. An attacker must first obtain the ability to execute code on the guest OS in order to exploit this vulnerability. The specific flaw exists within the handling of the slirp networking. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code under the context of current user in the host OS.

## Additional Details

Qemu has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=1586245

## Disclosure Timeline

- 2018-04-27 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
