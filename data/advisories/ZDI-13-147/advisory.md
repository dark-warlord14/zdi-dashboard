# ZDI-13-147: VMware vCenter Chargeback Manager ImageUploadServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-147
- **ZDI-CAN:** ZDI-CAN-1852
- **Date:** 2013-06-27
- **CVE:** CVE-2013-3520
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMWare, Inc.
- **Affected Products:** vCenter Chargeback Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-147/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VMware vCenter Chargeback Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the ImageUploadServlet. This service exposes the functionality which contains a flaw that allows attackers to create files at arbitrary locations with attacker controlled data. This can be leveraged by an attacker gain to remote code execution under the context of SYSTEM.

## Additional Details

VMWare, Inc. has issued an update to correct this vulnerability. More details can be found at: http://www.vmware.com/security/advisories/VMSA-2013-0008.html

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
