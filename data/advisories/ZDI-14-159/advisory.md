# ZDI-14-159: (0Day) VMware vCenter Server Appliance Ruby vSphere Console Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-159
- **ZDI-CAN:** ZDI-CAN-2003
- **Date:** 2014-05-30
- **CVE:** CVE-2014-3790
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:H/Au:S/C:C/I:C/A:C
- **Affected Vendors:** VMWare, Inc.
- **Affected Products:** VMWare vCenter Server Appliance
- **Credit:** Shanon Olsson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-159/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VMware vCenter Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the usage of the Ruby vSphere Console (RVC) provided by the vCenter Server Appliance. Commands can be run in a privileged context allowing an attacker to break-out of a chroot jail. This allows for an attacker to elevate privilege and execute commands as root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180-day deadline. Vendor Contact Timeline: 11/07/2013 - Case disclosed to vendor 11/07/2013 - Vendor acknowledged 12/02/2013 - Vendor confirmed reproduction 02/26/2014 - Vendor provided ETA August or September 05/02/2014 - Vendor provided ETA of August and December 05/02/2014 - ZDI asked vendor for something sooner 05/02/2014 - Vendor confirmed dates and will let ZDI know of any changes 05/06/2014 - Original 180-deadline passed 05/30/2014 - Public release of advisory -- Vendor Provided Mitigations: Remove all users from the shellaccess group with the following command: usermod -R shellaccess LOGIN OR Remove the line "AllowGroups shellaccess wheel" from the /etc/ssh/sshd_config Restart the sshd service with the following command: service sshd restart This issue only affects vCenter Server Appliance 5.1 and vCenter Server Appliance 5.5. No other products are affected by this issue.

## Disclosure Timeline

- 2013-11-07 - Vulnerability reported to vendor
- 2014-05-30 - Coordinated public release of advisory
