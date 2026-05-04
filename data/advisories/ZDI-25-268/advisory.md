# ZDI-25-268: GStreamer Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-268
- **ZDI-CAN:** ZDI-CAN-25448
- **Date:** 2025-04-30
- **CVE:** CVE-2025-2759
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GStreamer
- **Affected Products:** GStreamer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-268/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of GStreamer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Fixed in 1.25.1 Gstreamer Installer

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated
