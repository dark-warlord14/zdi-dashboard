# ZDI-22-1118: (Pwn2Own) Linux Kernel nft_object Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1118
- **ZDI-CAN:** ZDI-CAN-17470
- **Date:** 2022-08-18
- **CVE:** CVE-2022-2586
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Team Orca of Sea Security (@seasecresponse), security.sea.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1118/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of nft_objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://seclists.org/oss-sec/2022/q3/114

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
