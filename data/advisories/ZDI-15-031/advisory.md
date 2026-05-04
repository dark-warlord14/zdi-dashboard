# ZDI-15-031: VMware Workstation Authorization Service Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-031
- **ZDI-CAN:** ZDI-CAN-2383
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1044
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** VMware, Inc.
- **Affected Products:** VMware Workstation
- **Credit:** Dmitry Yudin @ret5et
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-031/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial-of-service on vulnerable installations of VMWare Workstation. Authentication is not required to exploit this vulnerability. The specific flaw exists within the VMWare Authorization service, which is listening on port 912. By sending a malformed packet, an attacker is able to cause the service to shut itself down. The service will not automatically restart, and once disabled virtual machines will not be able to get access to new resources.

## Additional Details

VMware, Inc. has issued an update to correct this vulnerability. More details can be found at: http://www.vmware.com/security/advisories/VMSA-2015-0001.html

## Disclosure Timeline

- 2014-07-17 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
