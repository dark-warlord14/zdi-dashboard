# ZDI-20-254: (Pwn2Own) Samsung Galaxy S10 FileWriter Use-After-Free Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-254
- **ZDI-CAN:** ZDI-CAN-9655
- **Date:** 2020-02-20
- **CVE:** N/A
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S10
- **Credit:** Pedro Ribeiro (pedrib@gmail.com) and Radek Domanski (radek.domanski@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-254/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Samsung Galaxy S10. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of arrays in FileWriterImpl::Write. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and escape the Chromium sandbox.

## Additional Details

Fixed in version 11.0.00.76

## Disclosure Timeline

- 2019-11-07 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
- 2020-02-21 - Advisory Updated
